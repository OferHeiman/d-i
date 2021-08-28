import random


class Gene:
	def __init__(self, value = 1):
		self.value = value

	def mutate(self, probability):
		self.value = random.choices([random.randrange(0, 2)], probability)


class Chromosome:
	def __init__(self, genes):
		if not len(genes) == 10:
			raise Exception("The chromosome must contain 10 genes")

		self.genes = genes

	def mutate(self, probability):
		for i in range(len(self.genes)):
			self.genes[i] = self.genes[i].mutate(probability)

	def is_all_ones(self):
		for gene in self.genes:
			if gene.value != 1:
				return False

		return True


class DNA:
	def __init__(self, chromosomes):
		if not len(chromosomes) == 10:
			raise Exception("The DNA must contain 10 chromosomes")

		self.chromosomes = chromosomes

	def mutate(self, probability: 0.5):
		for i in range(len(self.chromosomes)):
			self.chromosomes[i] = self.chromosomes[i].mutate(probability)
	
	def is_all_ones(self):
		for chromosome in self.chromosomes:
			if not chromosome.is_all_ones():
				return False

		return True


class Organism:
	def __init__(self, dna: DNA, probability):
		self.dna = dna
		self.probability = probability
		self.generations_count = 0

	def mutate(self):
		self.dna.mutate(self.probability)
		if self.dna.is_all_ones():
			print(f'the generations count is {self.generations_count}')
			return

		self.mutate()

gene = Gene()
gene.mutate(k=5)
print(gene)