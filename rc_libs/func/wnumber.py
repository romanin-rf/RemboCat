def dp_slice_float(var: float, count: int):
	VarDeс = str(var).split('.')
	if count == 0:
		return int(var)
	else:
		VarDeс[1] = VarDeс[1][:(count - len(VarDeс[1]))]
		return float(".".join(VarDeс))

