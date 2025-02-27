// filepath: /hike-tracker-app/hike-tracker-app/src/app.ts
import { HikeList, EquipmentList, HikeForm } from './components';
import { addHike, getHikes, addEquipment } from './services';
import { Hike, Equipment } from './models';

class HikeTrackerApp {
    private hikes: Hike[] = [];
    private equipment: Equipment[] = [];

    constructor() {
        this.initialize();
    }

    private initialize() {
        this.hikes = getHikes();
        this.render();
    }

    private render() {
        const hikeList = new HikeList(this.hikes);
        const equipmentList = new EquipmentList(this.equipment);
        const hikeForm = new HikeForm(this.addNewHike.bind(this), this.addNewEquipment.bind(this));

        document.body.appendChild(hikeList.render());
        document.body.appendChild(equipmentList.render());
        document.body.appendChild(hikeForm.render());
    }

    private addNewHike(hike: Hike) {
        addHike(hike);
        this.hikes = getHikes();
        this.render();
    }

    private addNewEquipment(equipment: Equipment) {
        addEquipment(equipment);
        this.equipment = []; // Update equipment list as needed
        this.render();
    }
}

const app = new HikeTrackerApp();