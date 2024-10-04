# api/views.py
from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.decorators import api_view
from .models import Pato, Cliente, Venda
from .serializers import PatoSerializer, ClienteSerializer, VendaSerializer
import openpyxl
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from django.http import FileResponse
from io import BytesIO

class PatoViewSet(viewsets.ModelViewSet):
    queryset = Pato.objects.all()
    serializer_class = PatoSerializer


class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer


class VendaViewSet(viewsets.ModelViewSet):
    queryset = Venda.objects.all()
    serializer_class = VendaSerializer

    def perform_create(self, serializer):
        venda = serializer.save()
        # Aqui você pode calcular o preço se necessário


@api_view(['GET'])
def gerar_relatorio_excel(request):
    # Criação de uma nova planilha
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Relatório de Vendas"

    # Cabeçalhos do relatório
    ws.append(["ID da Venda", "Cliente", "Data da Venda", "Valor Total"])

    # Adicionando os dados das vendas
    vendas = Venda.objects.all()
    if not vendas.exists():
        return HttpResponse("Nenhuma venda encontrada.", status=404)

    for venda in vendas:
        # Verificando se o cliente existe antes de acessar o nome
        cliente_nome = venda.cliente.nome if venda.cliente else "Cliente não encontrado"

        # Verificando se a data da venda existe
        data_venda = venda.data_venda.strftime('%Y-%m-%d %H:%M:%S') if venda.data_venda else "Data não disponível"

        # Adicionando a linha à planilha
        ws.append([venda.id, cliente_nome, data_venda, venda.valor_total()])

    # Salvando o conteúdo da planilha em um buffer
    buffer = BytesIO()
    wb.save(buffer)
    buffer.seek(0)

    # Configurações de resposta para download do arquivo
    response = HttpResponse(buffer, content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=relatorio_vendas.xlsx'
    return response


@api_view(['GET'])
def gerar_relatorio_pdf(request):
    buffer = BytesIO()
    p = canvas.Canvas(buffer, pagesize=letter)
    width, height = letter

    # Cabeçalho do relatório
    p.drawString(100, height - 50, "Relatório de Vendas")
    p.drawString(100, height - 80, "ID da Venda | Cliente | Data da Venda | Valor Total")

    # Adicionando os dados das vendas
    y = height - 100
    vendas = Venda.objects.all()
    for venda in vendas:
        p.drawString(100, y,
                     f"{venda.id} | {venda.cliente.nome} | {venda.data_venda.strftime('%Y-%m-%d %H:%M:%S')} | {venda.valor_total()}")
        y -= 20

    p.showPage()
    p.save()
    buffer.seek(0)

    return FileResponse(buffer, as_attachment=True, filename='relatorio_vendas.pdf')


def registrar_venda(request):
    return None


def listar_vendas(request):
    return None