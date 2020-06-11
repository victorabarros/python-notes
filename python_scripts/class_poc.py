from typing import Set


class TriggerRule:
    ALL_SUCCESS = 'all_success'
    ALL_FAILED = 'all_failed'
    ALL_DONE = 'all_done'
    ONE_SUCCESS = 'one_success'
    ONE_FAILED = 'one_failed'
    NONE_FAILED = 'none_failed'
    NONE_SKIPPED = 'none_skipped'
    DUMMY = 'dummy'

    _ALL_TRIGGER_RULES = set()  # type: Set[str]

    @classmethod
    def is_valid(cls, trigger_rule):
        return trigger_rule in cls.all_triggers()

    @classmethod
    def all_triggers(cls):
        if not cls._ALL_TRIGGER_RULES:
            cls._ALL_TRIGGER_RULES = {
                getattr(cls, attr)
                for attr in dir(cls)
                if not attr.startswith("_") and not callable(getattr(cls, attr))
            }
        return cls._ALL_TRIGGER_RULES

if __name__ == "__main__":
    i =TriggerRule.is_valid('none')
    import pdb; pdb.set_trace()