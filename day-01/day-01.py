import pandas as pd

df = pd.read_csv('input.txt', sep=' ', header=None)


def get_fuel(mass: int) -> int:
	fuel = int(mass // 3 - 2)
	if fuel > 0:
		return fuel
	return 0


df['fuel'] = df.apply(get_fuel, axis=1)

# part 1 solution
print(df['fuel'].sum())

# part 2 requires a while loop, which pandas isn't great at
# convert dataframe to list instead and use native python to solve
mass_list = df.loc[:, 0].values.tolist()

total = 0
for mass in mass_list:
	fuel = get_fuel(mass)
	while fuel > 0:
		total += fuel
		fuel = get_fuel(fuel)

print(total)
