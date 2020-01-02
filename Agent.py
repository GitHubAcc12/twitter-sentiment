from keras.models import Sequential
from keras.layers import Dense, Flatten
from keras.optimizers import Adam
from keras.models import model_from_json

import os.path
import numpy as np



class Agent:       

    def __init__(self, agent_id, input_dim=None, output_dim=None):
        self.learning_rate = 0.001
        self.epsilon = 0.00001
        self.agent_id = agent_id
        if input_dim==None or output_dim==None:
            if os.path.isfile('./data/model/model_' + self.agent_id +'.json'):
                self.load_existing_model()
            else:
                raise ValueError('No existing model, input and output_dim need to be specified')
        else:
            self.input_dim = input_dim
            self.output_dim = output_dim

            self.build_model()
        self.model.compile(loss='binary_crossentropy', optimizer='rmsprop')

    def build_model(self):
        if os.path.isfile('./data/model/model_' + self.agent_id + '.json'):
            self.load_existing_model()
            return
        self.model = Sequential()
        self.model.add(Dense(64, input_dim=self.input_dim, activation='relu'))
        self.model.add(Dense(32, activation='relu'))
        self.model.add(Dense(32, activation='relu')) # the 
        self.model.add(Dense(24, activation='relu')) # jkn
        self.model.add(Dense(24, activation='relu')) # the
        self.model.add(Dense(12, activation='relu')) # jkn
        self.model.add(Dense(self.output_dim, activation='sigmoid'))
        

    def save_model(self):
        # serialize model to JSON
        model_json = self.model.to_json()
        with open('./data/model/model_' + self.agent_id + '.json', 'w') as json_file:
            json_file.write(model_json)
        # serialize weights to HDF5
        self.model.save_weights('./data/model/model_' + self.agent_id + '.h5')
        print("Saved model to disk")

    def load_existing_model(self):
        with open('./data/model/model_' + self.agent_id + '.json', 'r') as json_file:
            loaded_model_json = json_file.read()
        self.model = model_from_json(loaded_model_json)
        # load weights into new model
        self.model.load_weights('./data/model/model_' + self.agent_id + '.h5')
        

    def classify(self, state):
        return self.model.predict(state)

    def train_on_batch(self, batch, verbose=0):
        error_rate = 1
        prev_error_rate = 0
        while error_rate > .15 and error_rate != prev_error_rate:
            prev_error_rate = error_rate
            wrong = 0
            states, targets = batch
            self.model.fit(states, targets, epochs=50, verbose=1, batch_size=128)
            for i in range(len(states)):
                state = np.array(states[i], dtype=float)
                state = state.reshape((1, len(state)))
                target_f = self.model.predict(state)
                if verbose == 1:
                    print(f'Predicted: {target_f}, actual: {targets[i]}')
                classification = target_f
                if abs(classification - targets[i]) > self.epsilon:
                    wrong += 1
            self.save_model()
            error_rate = wrong/len(states)
            print(f'Error Rate: {error_rate}')