import sqlalchemy as db
from flask import Flask,request,jsonify
from sqlalchemy.exc import SQLAlchemyError # this will help us to idenify error coming during the database activity

engine = db.create_engine('mysql://bobby:bobby_sabudh@13.233.98.174:3306/test_api')
connection = engine.connect()
metadata = db.MetaData()

Form = db.Table('Form', metadata, autoload=True, autoload_with=engine)# Here i am calling the two different table in order to give whole information  of given incident
FormInformation = db.Table('FormInformation', metadata, autoload=True, autoload_with=engine)
agri=Flask(__name__)

@agri.route("/insertform", methods=["Post"])
def insertform():
    user = request.get_json()
    user_name = user["UserName"]
    Date_time = user["Dot"]
    TofIncident = user["Typesofincident"]
    
    try:
        Record = Form.insert().values(UserName=user_name,Dot=Date_time,Typesofincident=TofIncident)
        ResultProxy = connection.execute(Record)
        return jsonify({"Succesfully enter the data ": user["UserName"]})
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        return jsonify({"It is a SQlAlchemyError":error})# this will give us relative error which help us to identify specific problem 
    except:
        return jsonify({"We dont know this error please contact the support team"})

@agri.route("/insertformIn",methods=["Post"])
def insertformIn():
    user = request.get_json()
    FormID = user["ID"]
    When_happend = user["Whenhappend"]
    where_happend = user["wherehappend"]
    How_happend = user["Howhappend"]
    No_of_Witness = user["NoofWitness"]
    witness_Name = user["witnessName"]
    suspect_Name = user["suspectName"]

    try:
        Record = FormInformation.insert().values(ID=FormID,Whenhappend=When_happend,wherehappend =where_happend,Howhappend = How_happend,NoofWitness=No_of_Witness,witnessName = witness_Name,suspectName=suspect_Name)
        ResultProxy = connection.execute(Record)
        return jsonify({"Succesfully enter the data Your ID is ": user["ID"]})
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        return jsonify({"It is a SQlAlchemyError": error})
    except:
        return jsonify({"We dont know this error please contact the support team"})


agri.run()
