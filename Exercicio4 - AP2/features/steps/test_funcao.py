from behave import given, when, then
from funcao import soma

@given('Primeiro valor será 5')
def step_primeiro_valor(context):
    context.a = 5

@given('segundo valor será 2')
def step_segundo_valor(context):
    context.b = 2

@when('executa a função')
def step_executa(context):
    context.resultado = soma(context.a, context.b)

@then('saida deverá ser o valor 7')
def step_verifica(context):
    assert context.resultado == 7, f'Esperado 7, mas obteve {context.resultado}'
