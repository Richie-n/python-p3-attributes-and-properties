#!/usr/bin/env python3

APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

class Person:
    
    def __init__(self, name= "Mike", job= "Sales"):
        self.name =name
        self.job =job
    
    def name(self):
        return self._name
    def set_name(self, name):
        if isinstance (name, str) and 1 <= len(name) <=25:
            self._name=name
        else:
            print("Name must be string between 1 and 25 characters.")

    name = property(name, set_name)

    def job(self):
        return self._job
    def set_job(self, job):
        if job in APPROVED_JOBS:
            self._job=job
        else:
             print("Job must be in list of approved jobs." )
        
    job = property(job, set_job)

new_worker = Person()

print(new_worker.name)
print(new_worker.job)
