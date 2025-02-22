from fastapi import APIRouter, Depends, HTTPException, status
from app.services.classify_service import detect_class
import logging

router = APIRouter()
logger = logging.getLogger("food_calorie_estimation")

model = YOLO("backend/app/ml_models/yolov8m_best.pt")

@router.get("/", tags=["classify"])
async def classify(file: UploadFile = File(...)):
    logger.info("Classify endpoint called")
    
    if model is None:
        logger.error("Model not loaded")
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="Model not loaded",
        )
    
    try:
        contents = await file.read()
        nparr = np.frombuffer(contents, np.uint8)
        img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

        results = model.predict(source=img)

        return {"detected_classes": detected_classes}

    except Exception as e:
        logger.error(f"Error in detecting class: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error in detecting class",
        )
