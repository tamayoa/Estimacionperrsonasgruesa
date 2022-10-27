    const Url = 'https://l3vy609ku1.execute-api.us-east-1.amazonaws.com/dev/espacios'
    const contenedor = document.querySelector('tbody')
    let resultados = ''
    
    
    const modalEspacio = new bootstrap.Modal(document.getElementById('modalEspacio'))
    const formEspacio = document.querySelector('form')
    const IdEspacio = document.getElementById('IdEspacio')
    const Oficina = document.getElementById('Oficina')
    const Sensor = document.getElementById('Sensor')
    const Tamaño = document.getElementById('Tamaño')
    const Cashiers = document.getElementById('Cashiers')
    var opcion = ''
    
    btnCrear.addEventListener('click', ()=>{
        IdEspacio.value = ''
        Oficina.value = ''
        Sensor.value = ''
        Tamaño.value = ''
        Cashiers.value = ''
        modalEspacio.show()
        opcion = 'crear'
    })
    
    
    const mostrar = (data) => {
        for(let i = 0; i < data.espacios.length; i++) {
            resultados += `<tr>
                                <td>${data.espacios[i].IdEspacio}</td>
                                <td>${data.espacios[i].Oficina}</td>
                                <td>${data.espacios[i].Sensor}</td>
                                <td>${data.espacios[i].Tamaño}</td>
                                <td>${data.espacios[i].Cashiers}</td>
                                <td class="text-center"><a class="btnEditar btn btn-primary">Edit</a><a class="btnBorrar btn btn-danger">Delete</a></td>
                           </tr>
                        `;    
        }
        contenedor.innerHTML = resultados
        
    }
    Parameters = {
        headers:{
            "Content-Type": "application/json; charset=UTF-8"
        },
    
         method:"GET"
    };
    
    fetch(Url, Parameters)
        .then(response => response.json())
        .then(data => { mostrar(data) })
    
    
        const on = (element, event, selector, handler) => {
              element.addEventListener(event, e => {
                if(e.target.closest(selector)){
                    handler(e)
                }
            })
        }
        
        //Borrar
        on(document, 'click', '.btnBorrar', e => {
            const fila = e.target.parentNode.parentNode
            var id = fila.firstElementChild.innerHTML
            
                var Data= JSON.stringify({
                    "IdEspacio": id
                })
    
                const Parameters = {
                    headers:{
                        "Content-Type": "application/json; charset=UTF-8"
                    },
                    method: 'DELETE',
                    body: Data
                    
                };
                fetch(Url, Parameters)
                .then( response => response.json() )
                .then( ()=> location.reload())
                
           
            
        })
        
        //Editar
       
        on(document, 'click', '.btnEditar', e => {    
            const fila = e.target.parentNode.parentNode
            const idForm = fila.children[0].innerHTML
            const oficinaForm = fila.children[1].innerHTML
            const sensorForm = fila.children[2].innerHTML
            const tamanoForm = fila.children[3].innerHTML
            const cashiersForm = fila.children[4].innerHTML
    
    
            //idForm = parseInt(idForm)
            IdEspacio.value = idForm
            Oficina.value =  oficinaForm
            Sensor.value =  sensorForm
            Tamaño.value =  tamanoForm
            Cashiers.value = cashiersForm
            opcion = 'editar'
            modalEspacio.show()
             
        })
        
         
        formEspacio.addEventListener('submit', (e)=>{
            e.preventDefault()
            if(opcion=='crear'){     
               
                var Data= JSON.stringify({
                    "IdEspacio": IdEspacio.value,
                    "Oficina": Oficina.value,
                    "Sensor": Sensor.value,
                    "Tamaño": Tamaño.value,
                    "Cashiers": Cashiers.value
                })
    
                const Parameters = {
                    headers:{
                        "Content-Type": "application/json; charset=UTF-8"
                    },
                    method: 'POST',
                    body: Data
                    
                };
                fetch(Url, Parameters)
                .then( response => response.json() )
                .then( ()=> location.reload())    
            
        }
            if(opcion=='editar'){    
                
                
                var Data= JSON.stringify({
                    "IdEspacio": IdEspacio.value,
                    "Oficina": Oficina.value,
                    "Sensor": Sensor.value,
                    "Tamaño": Tamaño.value,
                    "Cashiers": Cashiers.value
                })
    
                const Parameters = {
                    headers:{
                        "Content-Type": "application/json; charset=UTF-8"
                    },
                    method: 'POST',
                    body: Data
                    
                };
                fetch(Url, Parameters)
                .then( response => response.json() )
                .then( ()=> location.reload())      
            
            
        }
                modalEspacio.hide()
    
    
    
        })
