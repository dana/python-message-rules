import re
import os
import json
from message_match import mmatch
from message_transform import mtransform


class MessageRules:
    def __init__(self):
        self.loaded_configs = []
        self.rules = []

    def output_apply_rules(self, incoming_directory, outgoing_directory):
        messages = self.load_messages(incoming_directory)
        self.apply_rules(messages)
        for key, message in messages.items():
            try:
                with open(outgoing_directory + '/' + key, 'w') as outfile:
                    json.dump(message, outfile)
            except Exception as err:
                print('failed to write ' + key + ' in ' +
                      outgoing_directory + ': ' + str(err))
        return True

    def apply_rules(self, messages):
        out = {}
        for key, message in messages.items():
            self.merge_rules(message)
            out[key] = message
        return out

    def load_messages(self, directory):
        messages = {}
        for filename in self._recursive_file_gen(directory):
            print('loading ' + filename)
            try:
                message = json.loads(open(filename).read())
                key = filename.replace(directory, '')
                messages[re.sub(r"^/", '', key)] = message
            except Exception as err:
                print('failed to load ' + filename + ': ' + str(err))

        return messages

    def load_rules_from_directory(self, directory):
        for f in self._recursive_file_gen(directory):
            try:
                thing = json.loads(open(f).read())
                if isinstance(thing, dict):
                    if 'order' not in thing:
                        thing['order'] = 0
                    if 'is_not_a_rule' not in thing:
                        self.loaded_configs.append(thing)
                if isinstance(thing, list):
                    for message in thing:
                        if 'order' not in message:
                            message['order'] = 0
                        if 'is_not_a_rule' not in message:
                            self.loaded_configs.append(message)
            except:
                print('failed to load ' + f)
        self.rules = sorted(self.loaded_configs, key=lambda k: k['order'])
        return True

    def merge_rules(self, message):
        for conf in self.rules:
            if mmatch(message, conf['match']):
                mtransform(message, conf['transform'])
        return message

    def _recursive_file_gen(self, mydir):
        for root, dirs, files in os.walk(mydir):
            for file in files:
                yield os.path.join(root, file)
