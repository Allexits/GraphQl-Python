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


class CreateData(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
        title = graphene.String()
        description = graphene.String()

    data = graphene.Field(Data)
    
    def mutate(self,info,id,title,description):
        data = Data(id=id, title=title, description=description)
        return CreateData(data=data)


class Mutation(graphene.ObjectType):
    create_data = CreateData.Field()


class Query(graphene.ObjectType):
    data = graphene.Field(Data)


schema = graphene.Schema(query=Query, mutation=Mutation)
print(schema)

#===================== Query ==============
query_graphql= '''
mutation{
    createData(id:4, title:"d title", description:"4 d"){
        data{
            id
            title
            description
        }
    }
}
'''
#===================== Result =============
result = schema.execute(query_graphql)
print(json.dumps(result.data, indent=3))