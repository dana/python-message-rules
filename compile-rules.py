#!/usr/bin/python

from message_rules import MessageRules

r = MessageRules()
r.load_rules_from_directory('conf')
r.output_apply_rules('incoming', 'outgoing')
