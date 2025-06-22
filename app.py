<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>Asistente Cocina</title>
  <style>
    button {
      padding: 15px 25px;
      font-size: 18px;
      cursor: pointer;
      background-color: #4CAF50;
      border: none;
      color: white;
      border-radius: 5px;
      transition: background-color 0.3s ease;
    }
    button.loading {
      background-color: #999;
      cursor: wait;
    }
    button.success {
      background-color: #28a745;
    }
  </style>
</head>
<body>

  <button id="llamar-btn">Llamar al mesero</button>

  <script>
    const btn = document.getElementById('llamar-btn');

    btn.addEventListener('click', () => {
      btn.disabled = true;
      btn.classList.add('loading');
      btn.textContent = 'Enviando...';

      fetch('/llamar-mesero')
        .then(response => response.text())
        .then(text => {
          btn.classList.remove('loading');
          btn.classList.add('success');
          btn.textContent = '¡Mensaje enviado!';

          setTimeout(() => {
            btn.disabled = false;
            btn.classList.remove('success');
            btn.textContent = 'Llamar al mesero';
          }, 3000);
        })
        .catch(() => {
          btn.classList.remove('loading');
          btn.disabled = false;
          btn.textContent = 'Error, intenta otra vez';
          setTimeout(() => {
            btn.textContent = 'Llamar al mesero';
          }, 3000);
        });
    });
  </script>

</body>
</html>


