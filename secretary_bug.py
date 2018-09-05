import secretary

engine = secretary.Renderer()

result = engine.render(
    'template.odt',
    text={'Text': '1. One\n2. Two\n3. Three'}
)

output = open('output.odt', 'wb')
output.write(result)
output.close()
