﻿<%@ Page Language="vb" AutoEventWireup="false" CodeBehind="cad_Fornecedor.aspx.vb" Inherits="petshop_sis.cad_Fornecedor" %>

<!DOCTYPE html>

<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
<meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
    <title></title>
    <link href="../../Content/bootstrap.min.css" rel="stylesheet" />
</head>
<body>
  <div class="container">
    <div class="row">
      <div class="col-lg-10 col-xl-9 mx-auto">
        <div class="card card-signin flex-row my-5">
          <div class="card-img-left d-none d-md-flex">
             <!-- Background image for card set in CSS! -->
          </div>
          <div class="card-body">
            <h5 class="card-title text-center">Cadastrando Fornecedor</h5>
        
            <form class="form-signin">
  
              <div class="form-label-group">
                 <label for="inputUserame">NOME DA EMPRESA</label>
                <input type="text" id="inputUserame" class="form-control" placeholder="Nome da empresa" required autofocus>
                
              </div>

              <div class="form-label-group">
                <label for="inputEmail">CNPJ</label>
                <input type="number" id="inputEmail" class="form-control" required>
                
              </div>

              <div class="form-label-group">
                <label for="inputPassword">ENDEREÇO</label>
                <input type="text" id="inputPassword" class="form-control" placeholder="Endereço" required>
                
              </div>
              
              <div class="form-label-group">
                <label for="inputConfirmPassword">TELEFONE</label>
                <input type="number" id="inputConfirmPassword" class="form-control" placeholder="+00000000-0000" required>                
              </div>
              <hr />
              <button class="btn btn-lg btn-primary btn-block text-uppercase" type="submit">Cadastrar</button>
            </form>
          </div>
        </div>
      </div>
    </div>
  </div>
</body>
</html>
