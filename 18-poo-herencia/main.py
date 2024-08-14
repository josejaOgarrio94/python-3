import clases 

persona = clases.Persona()
persona.setNombre("Alex")
persona.setApellidos("González")
persona.setAltura("180cm")
persona.setEdad("30 años")
print("-------------------")

print(f"La persona es: {persona.getNombre()} {persona.getApellidos()}")
print(persona.hablar())
print(persona.caminar())
print(persona.dormir())

informatico = clases.Informatico()
informatico.setNombre("Alex")
informatico.setApellidos("González")
informatico.setAltura("180cm")
informatico.setEdad("30 años")
print(informatico.getLenguajes())
informatico.aprender("Python, JavaScript, PHP")

tecnico = clases.TecnicoRedes()
print(tecnico.auditarRedes)
