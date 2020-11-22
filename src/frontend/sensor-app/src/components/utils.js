export function filterRecordsByDate(records, startDateString, endDateString) {
    var recordsFiltered = [];
    if ((startDateString === '') && (endDateString === '')) {
        return records
    }
    else if ((startDateString !== '') && (endDateString !== '')) {
        const startDate = Date.parse(startDateString);
        const endDate = Date.parse(endDateString);
        recordsFiltered = records.filter(
            record => (record.timestamp * 1000) >= startDate && (record.timestamp * 1000) <= endDate
        )
    }
    else if (startDateString !== '') {
        const startDate = Date.parse(startDateString);
        recordsFiltered = records.filter(record => (record.timestamp * 1000) >= startDate)
    }
    else if (endDateString !== '') {
        const endDate = Date.parse(endDateString);
        recordsFiltered = records.filter(record => (record.timestamp * 1000) <= endDate)
    }
    return recordsFiltered
}

export function getDatetimesArray(sensorRecords) {
    var datetimes = [];
    sensorRecords.forEach((sensorRecord) => (
        datetimes.push(sensorRecord.datetime)
    ))
    return datetimes
}

export function getReadingsArray(sensorRecords) {
    var readings = [];
    sensorRecords.forEach((sensorRecord) => (
        readings.push(sensorRecord.reading)
    ))
    return readings
}