
'''Построить dict для позиций𝑘-mer’ов в геноме SARS-CoV-2 (𝑘–переменная).
При каком минимальном𝑘каждому фрагменту соответствует ровно одна позиция?'''


def kmers_dict(k, genome):
    positions = dict()
    for i in range(len(genome) - k):
        k_cur = genome[i: i + k]
        if k_cur not in positions.keys():
            positions[k_cur] = [i]
        else:
            positions[k_cur].append(i)
    return positions


with open('covid_gene.txt') as f:
    covid_genome = f.read().replace('\n', '')
k = int(input("enter the len of the k-mer: "))
positions = kmers_dict(k, covid_genome)

num_of_possible_kmers_in_dict = len(positions.keys())
num_of_all_pobbible_kmers = 4**k

print(num_of_possible_kmers_in_dict, num_of_all_pobbible_kmers)

print(positions)
