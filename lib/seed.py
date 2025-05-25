#!/usr/bin/env python3
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Company, Dev, Freebie

engine = create_engine('sqlite:///freebies.db')
Session = sessionmaker(bind=engine)
session = Session()

Base.metadata.create_all(engine)

company1 = Company(name="Google", founding_year=1998)
company2 = Company(name="Microsoft", founding_year=1975)

dev1 = Dev(name="Alice")
dev2 = Dev(name="Bob")

freebie1 = Freebie(item_name="Sticker", value=1, dev=dev1, company=company1)
freebie2 = Freebie(item_name="T-shirt", value=10, dev=dev2, company=company2)

session.add_all([company1, company2, dev1, dev2, freebie1, freebie2])
session.commit()

print("Database seeded successfully!")
