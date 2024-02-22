from abc import ABC, abstractmethod
from typing import List, Dict
from domain.entities.answer import Answer

class QuestionRepositoryInterface(ABC):
    @abstractmethod
    async def listQuestions() -> List[Dict]:
        raise NotImplementedError