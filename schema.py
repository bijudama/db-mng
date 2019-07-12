import sqlalchemy

metadata = sqlalchemy.MetaData()

templates = sqlalchemy.Table(
    'templates',
    metadata,
    sqlalchemy.Column('name', sqlalchemy.CHAR(length=70), primary_key=True),
    sqlalchemy.Column('activeVersion', sqlalchemy.INT(), server_default=sqlalchemy.text('1')),

    sqlalchemy.Column('t_createdAt', sqlalchemy.TIMESTAMP(), server_default=sqlalchemy.text('NOW()'), nullable=False),
    sqlalchemy.Column('t_updatedAt', sqlalchemy.TIMESTAMP(), server_default=sqlalchemy.text('NOW()'), nullable=False),
    sqlalchemy.Column('t_deletedAt', sqlalchemy.TIMESTAMP()),

    sqlalchemy.Column('t_createdBy', sqlalchemy.CHAR(length=30), nullable=False),
    sqlalchemy.Column('t_updatedBy', sqlalchemy.CHAR(length=30), nullable=False),
    sqlalchemy.Column('t_deletedBy', sqlalchemy.CHAR(length=30))
)

versions = sqlalchemy.Table(
    'versions',
    metadata,
    sqlalchemy.Column('number', sqlalchemy.INT(), primary_key=True),
    sqlalchemy.Column('templateName', sqlalchemy.ForeignKey("templates.name"), primary_key=True),

    sqlalchemy.Column('subject', sqlalchemy.TEXT(), nullable=False),
    sqlalchemy.Column('body', sqlalchemy.TEXT(), nullable=False),

    sqlalchemy.Column('fromEmail', sqlalchemy.CHAR(length=320), nullable=False),
    sqlalchemy.Column('replyToEmail', sqlalchemy.CHAR(length=320), nullable=False),

    sqlalchemy.Column('v_createdAt', sqlalchemy.TIMESTAMP(), server_default=sqlalchemy.text('NOW()'), nullable=False),
    sqlalchemy.Column('v_updatedAt', sqlalchemy.TIMESTAMP(), server_default=sqlalchemy.text('NOW()'), nullable=False),
    sqlalchemy.Column('v_deletedAt', sqlalchemy.TIMESTAMP()),

    sqlalchemy.Column('v_createdBy', sqlalchemy.CHAR(length=30), nullable=False),
    sqlalchemy.Column('v_updatedBy', sqlalchemy.CHAR(length=30), nullable=False),
    sqlalchemy.Column('v_deletedBy', sqlalchemy.CHAR(length=30))
)

def createSchema(insertFake = False):
    from config import Config
    engine = sqlalchemy.create_engine(Config.DB_URL)
    metadata.drop_all(engine)
    metadata.create_all(engine)
    if insertFake:
        conn = engine.connect()
        temps = [
            {'name': "temp1", 't_createdBy': "ammar1", 't_updatedBy': "ammar1"},
            {'name': "temp2", 't_createdBy': "ammar2", 't_updatedBy': "ammar2"},
            {'name': "temp3", 't_createdBy': "ammar3", 't_updatedBy': "ammar3"},
            {'name': "temp4", 't_createdBy': "ammar4", 't_updatedBy': "ammar4"},
            {'name': "temp5", 't_createdBy': "ammar5", 't_updatedBy': "ammar5"},
        ]
        conn.execute(templates.insert(), temps)

        vers = [
            {'templateName': "temp1", 'number': 1, 'v_createdBy': "AMMAR11", 'v_updatedBy': "AMMAR11", 'subject': "sub11", 'body': "bod11", 'fromEmail': "fe", 'replyToEmail': "reptoe"},
            {'templateName': "temp1", 'number': 2, 'v_createdBy': "AMMAR12", 'v_updatedBy': "AMMAR12", 'subject': "sub12", 'body': "bod12", 'fromEmail': "fe", 'replyToEmail': "reptoe"},
            {'templateName': "temp2", 'number': 1, 'v_createdBy': "AMMAR21", 'v_updatedBy': "AMMAR21", 'subject': "sub21", 'body': "bod21", 'fromEmail': "fe", 'replyToEmail': "reptoe"},
            {'templateName': "temp3", 'number': 1, 'v_createdBy': "AMMAR31", 'v_updatedBy': "AMMAR31", 'subject': "sub31", 'body': "bod31", 'fromEmail': "fe", 'replyToEmail': "reptoe"},
        ]

        conn.execute(versions.insert(), vers)

if __name__ == "__main__":
    createSchema(insertFake=True)





# import psycopg2
# con = psycopg2.connect(database="dynemailtemplates_1", user="postgres", password="159753", host="127.0.0.1", port="5432")
# cursor = con.cursor()
# createTemplateTable = '''CREATE TABLE Templates
#       (Name         CHAR(70) PRIMARY KEY NOT NULL UNIQUE,

#       Subject       TEXT            NOT NULL,
#       Body          TEXT            NOT NULL,

#       FromEmail          CHAR(320)       NOT NULL,
#       ReplyToEmail       CHAR(320)       NOT NULL,

#       ActiveVersion INT Default 1,

#       CreatedAt    TIMESTAMP       NOT NULL DEFAULT now(),
#       UpdatedAt    TIMESTAMP       NOT NULL DEFAULT now(),
#       DeletedAt    TIMESTAMP,

#       CreatedBy    CHAR(30),
#       UpdatedBy    CHAR(30),
#       DeletedBy    CHAR(30)
#       );'''


# createVersionTable = '''CREATE TABLE VERSIONS
#       (Number         INT NOT NULL,
#       TemplateName CHAR(70) NOT NULL,
#       Subject       TEXT            NOT NULL,
#       Body          TEXT            NOT NULL,

#       FromEmail          CHAR(320)       NOT NULL,
#       ReplyToEmail      CHAR(320)       NOT NULL,

#       CreatedAt    TIMESTAMP       NOT NULL DEFAULT now(),
#       UpdatedAt    TIMESTAMP       NOT NULL DEFAULT now(),
#       DeletedAt    TIMESTAMP,

#       CreatedBy    CHAR(30),
#       UpdatedBy    CHAR(30),
#       DeletedBy    CHAR(30),

#       FOREIGN KEY (TemplateName) REFERENCES Templates(Name),
#       PRIMARY KEY (Number, TemplateName)
#     );'''
# cursor.execute(createTemplateTable)
# cursor.execute(createVersionTable)
# con.commit()
# print("committed")
