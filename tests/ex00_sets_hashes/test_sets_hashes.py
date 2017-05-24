import related
from .models import Person, RoleModels


def test_set_construction():
    scientists = [Person(first_name="Grace", last_name="Hopper"),
                  Person(first_name="Katherine", last_name="Johnson"),
                  Person(first_name="Katherine", last_name="Johnson")]

    assert len(scientists) == 3

    role_models = RoleModels(scientists=scientists)
    assert len(role_models.scientists) == 2

    assert related.to_yaml(role_models).strip() in (SET_ORDER_1, SET_ORDER_2)


SET_ORDER_1 = """
scientists:
- first_name: Grace
  last_name: Hopper
- first_name: Katherine
  last_name: Johnson
""".strip()


SET_ORDER_2 = """
scientists:
- first_name: Katherine
  last_name: Johnson
- first_name: Grace
  last_name: Hopper
""".strip()
