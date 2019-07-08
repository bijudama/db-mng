from sanic.response import json
from schema import templates as templatesTable, versions as versionsTable
from sanic.response import dumps as defaultJsonDumps

from serialization import serializeTemplate, serializeTemplates


def setup(app):
    @app.route("/ammar")
    async def ammar(request):
        query = templatesTable.select()
        templatesRows = await request.app.db.fetch_all(query)
        print(dict(templatesRows[0]))
        return json({
            'templates': [{**dict(template), 'createdAt': 'now', 'updatedAt': 'now', 'deletedAt': 'now'} for template in templatesRows]
        })

    @app.route("/templates")
    async def getTemplates(request):
        query = templatesTable.select()
        templatesRows = await request.app.db.fetch_all(query)
        return json({
            'templates': serializeTemplates(templatesRows)
        })

    @app.route("/templates/<templateName>")
    async def getTemplate(request, templateName):
        query = templatesTable.select(whereclause=templatesTable.columns.name == templateName)
        templateRow = await request.app.db.fetch_all(query)
        templateRow = templateRow[0] if len(templateRow) > 0 else None
        return json({
            'template': serializeTemplate(templateRow)
        })

    @app.route("/templates/<templateName>/versions")
    async def getVersions(request, templateName):
        query = books.select()
        rows = await request.app.db.fetch_all(query)
        return json({
            'books': [{row['title']: row['author']} for row in rows]
        })

    @app.route("/templates/<templateName>/versions/versionNumber")
    async def getVersion(request, templateName, versionNumber):
        query = books.select()
        rows = await request.app.db.fetch_all(query)
        return json({
            'books': [{row['title']: row['author']} for row in rows]
        })
