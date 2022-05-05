import os
from dataloader import *

subject = 'M15'

data_root = "/ssd_scratch/cvit/kanishk/simplified_data/"

os.makedirs(data_root, exist_ok=True)

data_train, data_test, glove_train, glove_test, data_fine, data_fine_test, glove_fine, glove_fine_test = dataloader_sentence_word_split_new_matching_all_subjects(subject)

# print(data_train.shape, data_test.shape)

print(f'data_train: {data_train.shape}')
# np.save(data_root + 'data_train.npy', data_train)

print(f'data_test: {data_test.shape}')
# np.save(data_root + 'data_test.npy', data_test)

print(f'glove_train: {glove_train.shape}')
# np.save(data_root + 'glove_train.npy', glove_train)

print(f'glove_test: {glove_test.shape}')
# np.save(data_root + 'glove_test.npy', glove_test)

print(f'data_fine: {data_fine.shape}')
# np.save(data_root + 'data_fine.npy', data_fine)

print(f'data_fine_test: {data_fine_test.shape}')
# np.save(data_root + 'data_fine_test.npy', data_fine_test)

print(f'glove_fine: {glove_fine.shape}')
# np.save(data_root + 'glove_fine.npy', glove_fine)

print(f'glove_fine_test: {glove_fine_test.shape}')
# np.save(data_root + 'glove_fine_test.npy', glove_fine_test)

class_fine_test =np.eye(180)
class_fine = np.reshape(np.tile(class_fine_test,(42,1)),(7560,180))
class_fine_test = np.reshape(np.tile(class_fine_test,(3,1)),(540,180)) 
class_train = np.zeros((4530,180))

print(class_fine_test.shape, class_train.shape)


# data_train: (3903, 65730)
# data_test: (540, 65730)
# glove_train: (3903, 300)
# glove_test: (540, 300)
# data_fine: (7560, 65730)
# data_fine_test: (540, 65730)
# glove_fine: (7560, 300)
# glove_fine_test: (540, 300)
