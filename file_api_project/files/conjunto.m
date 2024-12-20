% Cargar los datos desde el archivo
filename = 'iris.data'; % Asegúrate de que este archivo esté en tu directorio actual
data = readtable(filename, 'Delimiter', ',', 'ReadVariableNames', false, 'FileType', 'text');

% Renombrar las columnas
data.Properties.VariableNames = {'SepalLength', 'SepalWidth', 'PetalLength', 'PetalWidth', 'Class'};

% Convertir características a matriz numérica
features = table2array(data(:, 1:4));
etiquetas = data.Class;

% Seleccionar dos clases 
clase1 = 'Iris-setosa';
clase2 = 'Iris-virginica';

% Filtrar datos por clase
indices_clase1 = strcmp(etiquetas, clase1);
indices_clase2 = strcmp(etiquetas, clase2);

features_clase1 = features(indices_clase1, :);
features_clase2 = features(indices_clase2, :);

% se escoge petalLength y petalWidth
x_feature = 3; % PetalLength
y_feature = 4; % PetalWidth

% Extraer las características para graficar
x_clase1 = features_clase1(:, x_feature);
y_clase1 = features_clase1(:, y_feature);

x_clase2 = features_clase2(:, x_feature);
y_clase2 = features_clase2(:, y_feature);

% Graficar los datos
figure;
hold on;
scatter(x_clase1, y_clase1, 'r', 'filled'); % Clase 1 en rojo
scatter(x_clase2, y_clase2, 'b', 'filled'); % Clase 2 en azul
legend(clase1, clase2);
title('Gráfica de dos clases del conjunto de datos Iris');
xlabel('Petal Length');
ylabel('Petal Width');
grid on;
hold off;
