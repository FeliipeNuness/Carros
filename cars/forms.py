from django import forms
from cars.models import Car


# Novo formulário simplificado
class CarModelForm(forms.ModelForm):

    class Meta:
        model = Car
        fields = '__all__'

    # Validação do valor
    def clean_value(self):
        value = self.cleaned_data.get('value')
        if value and value < 20000:  # Adiciona verificação se value não é None
            self.add_error('value', 'O valor mínimo do carro deve ser R$20.000')
        return value

    # Validação do ano de fabricação
    def clean_factory_year(self):
        factory_year = self.cleaned_data.get('factory_year')
        if factory_year and factory_year < 1975:  # Adiciona verificação se factory_year não é None
            self.add_error('factory_year', 'Não é possível cadastrar carros fabricados antes de 1975')
        return factory_year
