from sqlalchemy import Column, Integer, String, Date, Float, ForeignKey
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship
from database.config import engine_dw

Base = declarative_base()


class dLoss(Base):
    __tablename__ = 'dLoss'
    idLoss = Column(Integer, primary_key=True)
    LossDescription = Column(String(500), nullable=False)
    crm = relationship("fPipelineCRM", back_populates="dLoss")


class dPriority(Base):
    __tablename__ = 'dPriority'
    idPriority = Column(Integer, primary_key=True)
    PriorityDescription = Column(String(500), nullable=False)
    crm = relationship("fPipelineCRM", back_populates="dPriority")

class dStates(Base):
    __tablename__ = 'dStates'
    idStates = Column(Integer, primary_key=True)
    StatesDescription = Column(String(500), nullable=False)
    crm = relationship("fPipelineCRM", back_populates="dStates")

class dProducts(Base):
    __tablename__ = 'dProducts'
    idProducts = Column(Integer, primary_key=True)
    ProductDescription = Column(String(500), nullable=False)
    crm = relationship("fPipelineCRM", back_populates="dProducts")

class dContacts(Base):
    __tablename__ = 'dContacts'
    idContacts = Column(Integer, primary_key=True)
    Name = Column(String(500), nullable=False)
    Address = Column(String(500))
    City = Column(String(500))
    State = Column(String(500))
    Age = Column(Integer)
    Gender = Column(String(500))
    crm = relationship("fPipelineCRM", back_populates="dContacts")

class dCalender(Base):
    __tablename__ = 'dCalender'
    Date = Column(Date, primary_key=True)
    Year = Column(String(4), nullable=False)
    Month = Column(String(2))
    NameMonth = Column(String(20))
    Quarter = Column(String(3))
    Day = Column(Integer)
    WeekDay = Column(String(100))
    crm = relationship("fPipelineCRM", back_populates="dCalender")


class fPipelineCRM(Base):
    __tablename__ = 'fPipelineCRM'
    idCrm = Column(Integer, primary_key=True)
    DateOpen = Column(Date, ForeignKey("dCalender.Date"))
    DateClosed = Column(Date, ForeignKey("dCalender.Date"))
    idContacts = Column(Integer,ForeignKey("dContacts.idContacts"))
    idProducts = Column(Integer,ForeignKey("dProducts.idProducts"))
    idLoss = Column(Integer,ForeignKey("dLoss.idLoss"))
    idPriority = Column(Integer,ForeignKey("dPriority.idPriority"))
    idStage = Column(Integer,ForeignKey("dStates.idStates"))
    Interest = Column(String(500))
    QtdPeople = Column(Integer)
    Value = Column(Float)

    dLoss = relationship("dLoss", back_populates="crm")
    dPriority = relationship("dPriority", back_populates="crm")
    dStates = relationship("dStates", back_populates="crm")
    dProducts = relationship("dProducts", back_populates="crm")
    dContacts = relationship("dContacts", back_populates="crm")
    dCalender = relationship("dCalender", back_populates="crm")


Base.metadata.drop_all(bind=engine_dw)
Base.metadata.create_all(engine_dw)


def create_tables():
    Base.metadata.create_all(engine_dw)


if __name__ == "__main__":
    create_tables()
