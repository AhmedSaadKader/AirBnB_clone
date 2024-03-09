#!/usr/bin/python3
""" 5-main """
from models.base_model import BaseModel

if __name__ == "__main__":

    r1 = BaseModel()
    print(r1.created_at)
    print(r1.to_dict())
