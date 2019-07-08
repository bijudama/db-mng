import sqlalchemy

metadata = sqlalchemy.MetaData()

templates = sqlalchemy.Table(
    'templates',
    metadata,
    sqlalchemy.Column('name', sqlalchemy.CHAR(length=70), primary_key=True),
    sqlalchemy.Column('activeVersion', sqlalchemy.INT(), server_default=sqlalchemy.text('1')),

    sqlalchemy.Column('createdAt', sqlalchemy.TIMESTAMP(), server_default=sqlalchemy.text('NOW()'), nullable=False),
    sqlalchemy.Column('updatedAt', sqlalchemy.TIMESTAMP(), server_default=sqlalchemy.text('NOW()'), nullable=False),
    sqlalchemy.Column('deletedAt', sqlalchemy.TIMESTAMP()),

    sqlalchemy.Column('createdBy', sqlalchemy.CHAR(length=30), nullable=False),
    sqlalchemy.Column('updatedBy', sqlalchemy.CHAR(length=30), nullable=False),
    sqlalchemy.Column('deletedBy', sqlalchemy.CHAR(length=30))
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

    sqlalchemy.Column('createdAt', sqlalchemy.TIMESTAMP(), server_default=sqlalchemy.text('NOW()'), nullable=False),
    sqlalchemy.Column('updatedAt', sqlalchemy.TIMESTAMP(), server_default=sqlalchemy.text('NOW()'), nullable=False),
    sqlalchemy.Column('deletedAt', sqlalchemy.TIMESTAMP()),

    sqlalchemy.Column('createdBy', sqlalchemy.CHAR(length=30), nullable=False),
    sqlalchemy.Column('updatedBy', sqlalchemy.CHAR(length=30), nullable=False),
    sqlalchemy.Column('deletedBy', sqlalchemy.CHAR(length=30))
)

def createSchema():
    from config import Config
    engine = sqlalchemy.create_engine(Config.DB_URL)
    metadata.drop_all(engine)
    metadata.create_all(engine)

def test():
    from sqlalchemy import alias
    sa = sqlalchemy
    query = sa.select([alias(templates.c.createdAt, name="NewCreatedAt"), versions], sa.and_(templates.c.name == versions.c.templateName, templates.c.activeVersion == versions.c.number))
    print(query.__str__())
    
if __name__ == "__main__":
    createSchema()
    # test()





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
