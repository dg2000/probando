fecha_manchas.pdf: grafica.py fecha_manchas.dat
	python grafica.py


fecha_manchas.dat : monthrg.dat procesa.py
	python procesa.py

monthrg.dat:
	wget https://raw.githubusercontent.com/ComputoCienciasUniandes/MetodosComputacionalesDatos/master/hands_on/solar/monthrg.dat
