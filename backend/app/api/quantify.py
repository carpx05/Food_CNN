from fastapi import APIRouter, Depends, HTTPException, status
import logging

router = APIRouter()
logger = logging.getLogger("food_calorie_estimation")

CALORIE_MAP = {
    "banana": 89,
    "egg": 155,
    "idli": 58,
    "bread": 265,
    "dosa": 168
}

@router.post("/", tags=["quantify"])
async def calculate_calories(file: UploadFile = File(...)):
    logger.info("Calories endpoint called")

    try:
        detected_classes = await classify(file)

        total_calories = sum(CALORIE_MAP.get(food, 0) for food in detected_classes["detected_classes"])

        return {
            "detected_classes": detected_classes["detected_classes"],
            "estimated_calories": total_calories
        }

    except Exception as e:
        logger.error(f"Error in calorie calculation: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error in calorie calculation",
        )