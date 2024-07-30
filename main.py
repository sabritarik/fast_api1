from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Student(BaseModel):
    id: int
    name: str
    grade:str

Students = [
    Student(id=1,name="Ali",grade="A1"),
    Student(id=2,name="Mohamed",grade="A2"),
    Student(id=3,name="Sara",grade="A3")
    ]

@app.get("/students/")
def read_students():
    return Students

@app.post("/students/")
def create_student(New_Student:Student):
    Students.append(New_Student)
    return New_Student
@app.put("/students/{student_id}")
def update_student(student_id:int,updated_student:Student):
    for index, student in enumerate(Students):
        if student.id == student_id:
            Students[index] = updated_student
            return updated_student
    return {"error":"Student not found"}

@app.delete("/students/{student_id}")
def delete_student(student_id:int):
    for index,student in enumerate(Students):
        if student_id == student.id:
            del Students[index]
            return {"message":"Student deleted"}
    return {"error":"Student not found"}