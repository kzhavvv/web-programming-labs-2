function fillGoodList() {
    fetch('/rgz/api/goods/')
    .then(function (data) {
        return data.json();
    })
    .then(function (goods) {
        let tbody = document.getElementById('good-list');
        tbody.innerHTML = '';
        for(let i = 0; i<goods.length; i++) {
            let tr = document.createElement('tr');

            let tdName = document.createElement('td');
            tdName.innerText = goods[i].name;

            let tdArt = document.createElement('td');
            tdArt.innerText = goods[i].art;

            let tdCount = document.createElement('td');
            tdCount.innerText = goods[i].count;

            let tdPrice = document.createElement('td');
            tdPrice.innerText = goods[i].price;

            let tdCreatedAt = document.createElement('td'); // Добавляем элемент для даты создания
            tdCreatedAt.innerText = new Date(goods[i].createdAt).toLocaleDateString();

            let editButton = document.createElement('button');
            editButton.innerText = 'редактировать';
            editButton.onclick = function() {
                editGood(i, goods[i]);
            };

            let delButton = document.createElement('button');
            delButton.innerText = 'удалить';
            delButton.onclick = function() {
                deleteGood(i);
            };

            let tdActions = document.createElement('td');
            tdActions.append(editButton);
            tdActions.append(delButton);

            tr.append(tdName);
            tr.append(tdCount);
            tr.append(tdPrice);
            tr.append(tdArt);
            tr.append(tdActions);
            tr.append(tdCreatedAt); // Добавляем ячейку с датой создания

            tbody.append(tr);
        }
    })
}

function deleteGood(num) {
    if (! confirm('Вы точно хотите удалить товар?'))
        return;
    fetch(`/rgz/api/goods/${num}`, {method: 'DELETE'})
    .then(function () {
        fillGoodList();
    });
}

function showModal() {
    document.querySelector('div.modal').style.display = 'block';
}

function hideModal() {
    document.querySelector('div.modal').style.display = 'none';
}

function cancel() {
    hideModal();
}

function addGood() {
    showModal();
}

function addGood() {
    const good = {}; // Добавляем переменную goods
    delete good.createdAt;
    document.getElementById('num').value = '';
    document.getElementById('name').value = '';
    document.getElementById('art').value = '';
    document.getElementById('count').value = '';
    document.getElementById('price').value = '';
    showModal();
}

function sendGood() {
    const num = document.getElementById('num').value;
    const good = {
        name: document.getElementById('name').value,
        art: document.getElementById('art').value,
        count: document.getElementById('count').value,
        price: document.getElementById('price').value,
        createdAt: new Date().toString()
    };

    const url = `/rgz/api/goods/${num}`;
    const method = num ? 'PUT' : 'POST';
    fetch(url, {
        method: method,
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(good)
    })
    .then(function () {
        fillGoodList();
        hideModal();
    });
}


function editGood(num, good) {
    currentGood = good;
    document.getElementById('num').value = num;
    document.getElementById('name').value = good.name;
    document.getElementById('art').value = good.art;
    document.getElementById('count').value = good.count;
    document.getElementById('price').value = good.price;
    delete good.createdAt;
    showModal();
}