import numpy as np

class features():
    max_energy = 0
    max_centroid = 0
    min_centroid = 1000000
    max_spread = 0
    min_spread = 10**9
    max_entropy = 0
    min_entropy = 0

    def __init__(self):
        pass

    def compute_energy(self, fft, K):
        energy = 0
        for k in range(K):
            energy += pow(np.abs(fft[k]), 2)
        if energy > self.max_energy:
            self.max_energy = energy
        return energy, self.max_energy

    def compute_centroid(self, f, fft, K):
        numerator = 0
        denominator = 0 + np.nextafter(0, 1)
        for k in range(K):
            numerator += f[k] * np.abs(fft[k])
            denominator += np.abs(fft[k])
        centroid = numerator/denominator
        if centroid > self.max_centroid:
            self.max_centroid = centroid
        if centroid < self.min_centroid:
            self.min_centroid = centroid
        return centroid, self.max_centroid, self.min_centroid

    def compute_spread(self, f, fft, K, centroid):
        numerator = 0
        denominator = 0 + np.nextafter(0, 1)
        for k in range(K):
            numerator += pow((f[k] - centroid), 2) * np.abs(fft[k])
            denominator += np.abs(fft[k])
        spread = numerator/denominator
        if spread > self.max_spread:
            self.max_spread = spread
        if spread < self.min_spread:
            self.min_spread = spread
        return spread, self.max_spread, self.min_spread

    def compute_entropy(self, fft, K):
        numerator = 0
        denominator = np.log(K)
        for k in range(K):
            numerator -= np.abs(fft[k]) * np.log(np.abs(fft[k]) + 0.00001)
        entropy = numerator/denominator
        if entropy < self.min_entropy:
            self.min_entropy = entropy
        if entropy > self.max_entropy:
            self.max_entropy = entropy
        return entropy, self.min_entropy, self.max_entropy

    def compute_features(self, f, fft, K):
        features = []

        energy, max_energy = self.compute_energy(fft, K)
        features.append([energy, max_energy])

        centroid, max_centroid, min_centroid = self.compute_centroid(f, fft, K)
        features.append([centroid, max_centroid, min_centroid])

        spread, max_spread, min_spread = self.compute_spread(f, fft, K, centroid)
        features.append([spread, max_spread, min_spread])

        entropy, min_entropy, max_entropy = self.compute_entropy(fft, K)
        features.append([entropy, min_entropy, max_entropy])

        return features