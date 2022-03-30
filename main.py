from vagas import Veiculo, Enviar

veiculo = Veiculo('Ford Fiesta', 'Edificio Garagem', '15')
enviar = Enviar(veiculo)
print(enviar.notificar())