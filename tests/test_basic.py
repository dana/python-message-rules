import shutil
import sys
import os
import json
sys.path.append('..')
sys.path.append('.')
from message_rules import MessageRules  # noqa: E402


def test_simplest_merge():
    r = MessageRules()
    assert r.load_rules_from_directory('tests/conf')
    message = r.merge_rules({'main': 'thing'})
    assert message['this'] == 'that'


def test_apply_rules():
    r = MessageRules()
    assert r.load_rules_from_directory('tests/conf')
    messages = r.load_messages('tests/incoming')
    assert r.apply_rules(messages)
    assert messages['one.conf']['this'] == 'that'


def test_output_apply_rules():
    try:
        shutil.rmtree('/tmp/message-rules')
    except Exception:
        pass

    os.mkdir('/tmp/message-rules')
    r = MessageRules()
    assert r.load_rules_from_directory('tests/conf')
    assert r.output_apply_rules('tests/incoming', '/tmp/message-rules')
    message = json.loads(open('/tmp/message-rules/one.conf').read())
    assert message['main'] == 'thing'
    assert message['this'] == 'that'
