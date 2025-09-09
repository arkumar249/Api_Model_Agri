from fastapi import APIRouter, Query, HTTPException
from typing import Optional , List

from pydantic import BaseModel
from datetime import date
from uuid import UUID
from core.database import supabase
from Models.plant_disease_detector import run_pipeline
from Models.crop_recommendation import predict_crop_llm
from Models.Fertilizer_Recommender.fertilizer_recommender import recommend_fertilizers

from main import logger


class Token(BaseModel):
    refresh_token:str
    token_type:str

class TokenData(BaseModel):
    id:Optional[str] = None

class CropRequest(BaseModel):
    temperature: float
    humidity: float
    rainfall: float
    soilPh: float
    nitrogen: float
    phosphorus: float
    potassium: float
    soilType: str
    season: str


class CropResponse(BaseModel):
    name: str
    percent: int
    short_detail: str
    long_detail: str

class FertilizerRequest(BaseModel):
    temperature: int
    humidity: int
    rainfall: int
    soilPh: float
    nitrogen: int
    phosphorus: int
    potassium: int
    soilType: str
    season: str

class DetailedDescription(BaseModel):
    benefits: List[str]
    precautions: List[str]

class FertilizerRecommendation(BaseModel):
    fertilizer: str
    confidence: float
    short_description: str
    detailed_description: DetailedDescription

class FertilizerResponse(BaseModel):
    recommendations: List[FertilizerRecommendation]


router = APIRouter(prefix="/api_model", tags=["api_model"])

class AnalyzeRequest(BaseModel):
    image_url: str
    crop: Optional[str] = ""
    description: Optional[str] = ""

@router.post("/pest_detection_and_analyze")
async def analyze(req: AnalyzeRequest):
    # For now return dummy response
    response=run_pipeline(req.image_url, req.description)
    return response



@router.post("/crop_recommendations", response_model=List[CropResponse])
async def get_crop_recommendations(payload: CropRequest):
    raw = predict_crop_llm(payload.nitrogen, payload.phosphorus, payload.potassium,
                     payload.temperature, payload.humidity, payload.soilPh, payload.rainfall)

    transformed = []
    for item in raw["recommendations"]:
        transformed.append(CropResponse(
            name=item["crop"],                        # map crop → name
            percent=int(item.get("confidence", 0)),   # map confidence → percent
            short_detail=item.get("short_description", ""),
            long_detail=item.get("detailed_description", {}).get("irrigation", "")
        ))
    return transformed


@router.post("/fertilizer_recommendation", response_model=FertilizerResponse)
async def get_fertilizer_recommendation(request: FertilizerRequest):
    try:
        result=recommend_fertilizers(
            N=request.nitrogen,
            P=request.phosphorus,
            K=request.potassium,
            temperature=request.temperature,
            humidity=request.humidity,
            ph=request.soilPh,
            rainfall=request.rainfall,
            crop=request.soilType,
            verbose=False   
        )

        return result["structured"]

    except Exception as e:
        logger.error(f"Fertilizer recommendation failed: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")