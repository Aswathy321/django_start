//<script>
    function getdata() {
        var xhttp = new XMLHttpRequest()
        xhttp.open("GET","/home_2/getall/" + document.getElementById('keyword').value,true)
        xhttp.onreadystatechange = function(){
            if (this.readyState == 4 && this.status == 200){
               var data = JSON.parse(this.responseText);
               console.log(data)
               str = '<table>'

               for (x of data.pros){
                    str = str + '<tr>'
                    str = str + '<td>' + (x.id) +'-'+ '<td>'
                    str = str + '<td>' + (x.name) +'='+ '<td>'
                    str = str + '<td>' +'='+ (x.price) + '<td>'
                }
                str = str + '</table>'
                document.getElementById('data').innerHTML = str
           }
        };
       xhttp.send();
    }

function drawchart(){
            var xhttp = new XMLHttpRequest()
            xhttp.open("GET","/home_2/gap",true)
            xhttp.onreadystatechange = function() {
                if (this.readyState == 4 && this.status ==200) {
                    var data = JSON.parse(this.responseText);
                    displayChart(data)
                 }
            };
            xhttp.send();
         }
         function displayChart(data) {
                 var ctx = document.getElementById('Charts').getContext('2d');
                 var chart = new Chart(ctx, {
            // The type of chart we want to create
            type: 'bar',
                // axisX: {title:"iPhones",titleFontFamily:"comic sans ms"}
                // axisY: {title:"Price",titleFontFamily:"comic sans ms"}
            // The data for our dataset
            data: {
                 labels: get_labels(data),
                 datasets: [{
                     label: 'Products',
                     backgroundColor: 'rgb(255, 99, 132)',
                     borderColor: 'rgb(255, 99, 132)',
                     data: get_vals(data)
                 }]
            },

            // Configuration options go here
            options: {}
         });
       }
       function get_labels(data) {
           let labels = []
           for (x of data.pros) {
               labels.push(x.name)
           }
           return labels
      }
      function get_vals(data) {
           let vals = []
           for (x of data.pros) {
               vals.push(x.price)
           }
           return vals
      }
//</script>