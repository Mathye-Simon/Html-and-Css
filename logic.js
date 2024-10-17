const tech = document.querySelector('.tech')
const values = {'Microsoft-Office': 75,'Javascript': 70, 'HTML': 70, 'GitHub': 70, 'CSS': 60,
                'Python': 50, 'Git': 50, 'Express-js': 50, 'MYSQL-Database': 40, 'Node-js': 40, 'SQL': 30}

function createBarFill(values) {

    
    Object.entries(values).forEach(value => {
        // dom manipulation for each object pair
        let progressBarContainer = document.createElement('div')
        progressBarContainer.setAttribute('class', 'progress-bar-container');
        let progressBarFill = document.createElement("div");
        let progressBarLabel = document.createElement('div');
        let titles = document.createElement('div')
        titles.textContent = `${value[0]}`
        titles.setAttribute('class', 'titles')

        let id = value[0]
        progressBarFill.setAttribute('class', 'progress-bar-fill')
        progressBarLabel.setAttribute('class', 'progress-bar-label')
        width = value[1]
        

        progressBarFill.style.width = `${width}%`;
        progressBarLabel.textContent = width;
        
        // logic for gauge
            if (width >= 0 && width <= 30) {
                progressBarFill.style.backgroundColor = 'red';
            } 
            else if (width >= 30 && width <= 60) {
                progressBarFill.style.backgroundColor = 'orange';
            } 
            else if (width >= 60 && width <= 99) {
                progressBarFill.style.backgroundColor = 'green';
            } 


        progressBarContainer.append(progressBarFill, progressBarLabel)
        titles.append(progressBarContainer)
        tech.append(titles)
        // console.log(progressBarContainer)
    });
}
// call
createBarFill(values)

