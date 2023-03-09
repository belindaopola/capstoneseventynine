from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os

# Create object of ChatBot class with Storage and Logic Adapter
bot = ChatBot('Karty',
              storage_adapter='chatterbot.storage.SQLStorageAdapter',
              logic_adapters=[
                  'chatterbot.logic.BestMatch',
                  {
                      'import_path': 'chatterbot.logic.BestMatch',
                      'default_response': 'I am sorry, but I do not understand. I am still learning.',
                      'maximum_similarity_threshold': 0.90
                  }
              ],
              filters=[
                  'chatterbot.filters.RepetitiveResponseFilter'
              ],
              input_adapter='chatterbot.input.TerminalAdapter',
              output_adapter='chatterbot.output.TerminalAdapter',
              database='conversations',
              database_uri='mysql+pymysql://admin:3X47Qy!b@projectkarty.cmoarzscfdhk.eu-west-2.rds.amazonaws.com'
                           '/conversations'
              )

# # Training With Own Questions
trainer = ListTrainer(bot)
for file in os.listdir('data'):
    print('Training using ' + file)
    training_data = open('data/' + file).readlines()
    trainer.train(training_data)
    print("Training completed for " + file)
