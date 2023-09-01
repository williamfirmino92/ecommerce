from django.db import models

# Create your models here.
class Produto(models.Model):
    nome = models.CharField(max_length=255)
    descricao_curta = models.TextField(max_length=255)
    descricao_longa = models.TextField()
    imagem = models.ImageField(upload_to='produto_imagens', blank=True)
    slug = models.SlugField(unique=True)
    preco_marketing = models.FloatField(verbose_name='Preço')
    preco_marketing_promocional = models.FloatField(default=0, verbose_name='Preço Promocional')
    tipo = models.CharField(
        default='V',
        max_length=1,
        choices=(
            ('V', 'Variação'),
            ('S', 'Simples'),
        )
    )
    
    def get_preco_formatado(self):
        return f'R$ {self.preco_marketing:.2f}'
    get_preco_formatado.short_description = 'Preço'
    
    def get_preco_promocional_formatado(self):
        return f'R$ {self.preco_marketing_promocional:.2f}'
    get_preco_promocional_formatado.short_description = 'Preço Promo'
    
    def __str__(self):
        return f'{self.nome}'
    

class Variacao(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    nome = models.CharField(max_length=255)
    preco_marketing = models.FloatField()
    preco_marketing_promocional = models.FloatField(default=0)
    estoque = models.PositiveIntegerField(default=1)
    
    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = 'Variação'
        verbose_name_plural = 'Variações'
    
    
    
    
    
    
    
    
    