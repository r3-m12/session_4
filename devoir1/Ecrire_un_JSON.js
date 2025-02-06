<!DOCTYPE html>
<html>
    <body>
        
        <h2>Écrire un JSON</h2>
        
        <p id="exemple"></p>

        <script>
            let tetxt = '{"personnes" :[' +
            '{"prénom" : "nomA1", "nomfamille" : "nomA2" },' 
            +
            '{"prénom":"nomB1","nomfamille":"nomB2" },' 
            + 
            '{"firprénom":"nomC1","nomfamille":"nomC2" }]}';

            const obj = JSON.parse(text); 
            document.getElementById("exemple").innerHTML = 
            obj.personnes[1].prénom + " " + obj.personnes[1].nomfamille;
        </script>
    </body>
</html>