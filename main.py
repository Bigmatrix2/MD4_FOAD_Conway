import numpy as np

# Initialisation de la grille
frame = np.array([
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0]
])

def compute_number_neighbors(padded_frame, index_line, index_column):
    """
    Calcule le nombre de voisins vivants pour une cellule donnée.
    """
    return np.sum(padded_frame[index_line-1:index_line+2, index_column-1:index_column+2]) - padded_frame[index_line, index_column]

def compute_next_frame(frame):
    """
    Calcule la frame suivante selon les règles du jeu de la vie.
    """
    # Ajout de bordures de padding
    padded_frame = np.pad(frame, 1, mode="constant")
    
    # Parcours de la matrice avec bordure
    for first_number in range(1, padded_frame.shape[0] - 1):
        for second_number in range(1, padded_frame.shape[1] - 1):
            # Calcul des voisins vivants
            num_neighbors = compute_number_neighbors(padded_frame, first_number, second_number)

            # Application des règles du jeu de la vie
            if padded_frame[first_number, second_number] == 1:  # Cellule vivante
                if num_neighbors < 2 or num_neighbors > 3:
                    frame[first_number-1, second_number-1] = 0  # Meurt
            else:  # Cellule morte
                if num_neighbors == 3:
                    frame[first_number-1, second_number-1] = 1  # Devient vivante

    return frame

# Boucle infinie pour afficher les frames successives
while True:
    print(frame)
    frame = compute_next_frame(frame)