from pydantic import BaseModel
from typing import List

# class QueryResult(BaseModel):
#     columns: list[str]
#     rows: list[list[any]]
#     row_count: int
#     execution_time_ms: float
#     query_type: str
#     message: Optional[str] = None



class MessagePart(BaseModel):
    type: str  
    text: str


class Message(BaseModel):
    id: str
    role: str 
    parts: List[MessagePart]

class ChatPayload(BaseModel):
    id: str
    messages: List[Message]
    trigger: str



# class CoachResponse(BaseModel):
#     response_type: Literal["plan", "answer", "fallback"]
#     plan_title: Optional[str] = None
#     summary: str
#     milestones: List[Milestone] = Field(default_factory=list)
#     weekly_schedule: List[WeekPlan] = Field(default_factory=list)
#     risks: List[RiskItem] = Field(default_factory=list)
#     next_actions: List[str] = Field(default_factory=list)
#     mesage_for_user: str