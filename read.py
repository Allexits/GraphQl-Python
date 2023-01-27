try:
    import json
    import graphene
    import os
    print('import packages')
except Exception as e:
    print('Error : {}'.format(e))

DATA = {
    "list":[
    {
     "id":1,
     "title":"title c",
     "description":"description first"
    },
    {
     "id":2,
     "title":"title b",
     "description":"description second"
    },
    {
     "id":3,
     "title":"title a",
     "description":"description third"
    }
]
}


class Data(graphene.ObjectType):
    id = graphene.ID()
    title = graphene.String()
    description = graphene.String()


class Query(graphene.ObjectType):
    read_data = graphene.List(Data, order=graphene.String(default_value='id'))
    def resolve_read_data(root,info,order):
        sorted_obj = dict(DATA)
        sorted_obj['list'] = sorted(sorted_obj['list'], key=lambda x : x[order])
        data = sorted_obj
        return data['list']


schema = graphene.Schema(query=Query)
print(schema)

#===================== Query ==============
query_graphql= '''
query{
    readData{
        id
        title
        description
    }
}
'''
#===================== Result =============
result = schema.execute(query_graphql)
print(json.dumps(result.data, indent=3))