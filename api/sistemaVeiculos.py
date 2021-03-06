from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from util import mesesUnicos, gerarDict, toTuple

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/veiculos.db'
app.config['SECRET_KEY'] = 'secret'

db = SQLAlchemy(app)

class Veiculos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    marca = db.Column(db.String(20), nullable=False)
    modelo = db.Column(db.String(20), nullable=False)
    ano_fabricacao = db.Column(db.Integer, nullable=False)
    placa = db.Column(db.String(20), nullable=False)
    cor = db.Column(db.String(20), nullable=False)
    chassi = db.Column(db.String(17), nullable=False, unique=True)
    data_compra = db.Column(db.DATE, nullable=False)
    valor_compra = db.Column(db.REAL, nullable=False)

    def __init__(self, marca, modelo, anoF, placa, cor, chassi, dataC, valorC):
        self.marca = marca
        self.modelo = modelo
        self.ano_fabricacao = anoF
        self.placa = placa
        self.cor = cor
        self.chassi = chassi
        self.data_compra = dataC
        self.valor_compra = valorC

class VeiculosVendidos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    marca = db.Column(db.String(20), nullable=False)
    modelo = db.Column(db.String(20), nullable=False)
    ano_fabricacao = db.Column(db.Integer, nullable=False)
    placa = db.Column(db.String(8), nullable=False)
    cor = db.Column(db.String(20), nullable=False)
    chassi = db.Column(db.String(17), nullable=False, unique=True)
    data_compra = db.Column(db.DATE, nullable=False)
    valor_compra = db.Column(db.REAL, nullable=False)
    data_venda = db.Column(db.DATE, nullable=False)
    valor_venda = db.Column(db.REAL, nullable=False)

    def __init__(self, marca, modelo, anoF, placa, cor, chassi, dataC, valorC, dataV, valorV):
        self.marca = marca
        self.modelo = modelo
        self.ano_fabricacao = anoF
        self.placa = placa
        self.cor = cor
        self.chassi = chassi
        self.data_compra = dataC
        self.valor_compra = valorC
        self.data_venda = dataV
        self.valor_venda = valorV

@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route('/comprarVeiculo', methods=["GET", "POST"])
def comprarVeiculo():
    mensagem = ''
    if request.method == "POST":
        veiculo = Veiculos(request.form['marca'], request.form['modelo'], request.form['anoFabricacao'], request.form['placa'], request.form['cor'], request.form['chassi'], datetime.strptime(request.form['dataCompra'], '%Y-%m-%d').date(), request.form['valorCompra'])

        try:
            db.session.add(veiculo)
            db.session.commit()
            mensagem = 'Ve??culo cadastrado com sucesso! Voc?? pode conferi-lo na sess??o Ve??culos : Dispon??veis.'
        except:
            mensagem = 'FALHA! n??o foi poss??vel cadastrar o ve??culo, verifique os dados e tente novamente.'
        return render_template("comprarVeiculo.html", mensagem=mensagem)
        
    else:
        mensagem = 'Bem Vindo! Aqui voc?? pode registar a compra de um ve??culo!'   
        return render_template("comprarVeiculo.html", mensagem=mensagem)
    

@app.route('/historicoVendas')
def historicoVendas():
    veiculos = VeiculosVendidos.query.all()
    return render_template("historicoVendas.html", veiculos=veiculos)

@app.route('/listarVeiculos')
def listarVeiculos():
    veiculos = Veiculos.query.all()
    return render_template("listarVeiculos.html", veiculos=veiculos)

@app.route('/registrarVenda', methods=["GET", "POST"])
def registarVenda():
    mensagem = ''
    if request.method == "POST":

        try:
            getVeiculo = Veiculos.query.filter_by(chassi=request.form['chassi']).first()
            veiculo = VeiculosVendidos(getVeiculo.marca, getVeiculo.modelo, getVeiculo.ano_fabricacao, getVeiculo.placa, getVeiculo.cor, getVeiculo.chassi, getVeiculo.data_compra, getVeiculo.valor_compra, datetime.strptime(request.form['dataVenda'], '%Y-%m-%d').date(), request.form['valorVenda'])    

            db.session.delete(getVeiculo)
            db.session.commit()
            db.session.add(veiculo)
            db.session.commit()
            mensagem = 'Ve??culo vendido com sucesso! Voc?? pode conferi-lo na sess??o Ve??culos : Vendidos.'
        except:
            mensagem = 'FALHA! n??o foi poss??vel encontrar o ve??culo, verifique os dados e tente novamente.'
        return render_template("registrarVenda.html", mensagem=mensagem)
    else:
        mensagem = 'Bem Vindo! Aqui voc?? pode registar a venda de um ve??culo!'  
        return render_template("registrarVenda.html", mensagem=mensagem)   

@app.route('/relatorioMensal', methods=["GET", "POST"])
def relatorioMensal():
    
    getVeiculos = VeiculosVendidos.query.all()
    lista = []
    for x in getVeiculos:
        lista.append(x)
        
    meses = mesesUnicos(lista)

    if request.method == "POST":
        dicionario = gerarDict(meses, getVeiculos)
        req = toTuple(request.form['mes'])
        reqDic = dicionario[req]
        dia = []
        valorCompra = []
        valorVenda = []
        comissao = []
        for x in reqDic:
            dia.append(x.data_venda.day)
            valorCompra.append(x.valor_compra)
            valorVenda.append(x.valor_venda)
            if (x.valor_venda - x.valor_compra) > 0:
                comissao.append((x.valor_venda - x.valor_compra)*.1)
        return render_template("relatorioMes.html", dia=dia, valorCompra=valorCompra, valorVenda=valorVenda, comissao=comissao)
    
    return render_template("relatorioMensal.html", meses=meses)

if __name__ == '__main__':
    app.run(debug=True)
   

    

