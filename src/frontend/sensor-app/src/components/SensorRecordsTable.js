import React, { useMemo, useState } from 'react';
import { useTable, useSortBy, usePagination } from 'react-table';
import { filterRecordsByDate } from './utils';
import sensorRecords from '../data/sensorRecordsSnapshot.json';
import { COLUMNS } from './columns';
import './table.css';

export function SensorRecordsTable({ startDateString='', endDateString='' }) {
    const sensorRecordsToShow = filterRecordsByDate(sensorRecords, startDateString, endDateString);
    const data = useMemo(() => sensorRecordsToShow, []);
    const columns = useMemo(() => COLUMNS, []);
    const tableInstance = useTable({
        columns: columns,
        data: data,
    }, useSortBy, usePagination);
    const {
        getTableProps,
        getTableBodyProps,
        headerGroups,
        page,
        nextPage,
        previousPage,
        canNextPage,
        canPreviousPage,
        pageOptions,
        gotoPage,
        pageCount,
        setPageSize,
        state,
        prepareRow,
    } = tableInstance;
    const { pageIndex, pageSize } = state;

    return (
        <>
            <table {...getTableProps()}>
                <thead>
                    { headerGroups.map((headerGroup) => (
                        <tr {...headerGroup.getHeaderGroupProps()}>
                            { headerGroup.headers.map((column) => (
                                <th {...column.getHeaderProps(column.getSortByToggleProps())}>
                                    {column.render('Header')}
                                    <span>
                                        { column.isSorted ? (column.isSortedDesc ? ' (Desc)' : ' (Asc)') : '' }
                                    </span>
                                </th>
                            )) }
                        </tr>
                    )) }
                </thead>
        
                <tbody {...getTableBodyProps()}>
                    { page.map(row => {
                        prepareRow(row)
                        return (
                            <tr {...row.getRowProps()}>
                                { row.cells.map(cell => {
                                    return <td {...cell.getCellProps()}>{cell.render('Cell')}</td>
                                }) }
                            </tr>
                        )
                    }) }
                </tbody>
            </table>

            <div>
                <span>
                    Page {' '}
                    <strong>
                        { pageIndex + 1 } of { pageOptions.length }
                    </strong> {' '}
                </span>

                <span>
                    | Number of records: <strong>{ sensorRecordsToShow.length }</strong> {' '}
                </span>

                <span>
                    | Go to page: {' '}
                    <input type='number'
                           defaultValue={ pageIndex + 1 }
                           onChange={event => {
                               const value = event.target.value;
                               const pageNumber = value ? Number(value - 1) : 0
                               gotoPage(pageNumber)
                           }}
                           style={ {width: '50px'} }
                    />
                </span>

                <select value={pageSize} onChange={event => setPageSize(Number(event.target.value))}>
                    {
                        [10, 15, 30, 50].map(pageSize => (
                            <option key={pageSize} value={pageSize}>
                                Show { pageSize } records per page
                            </option>
                        ))
                    }
                </select>

                <button onClick={() => gotoPage(0)} disabled={!canPreviousPage}>{'<<'}</button>
                <button onClick={() => previousPage()} disabled={!canPreviousPage}>Previous</button>
                <button onClick={() => nextPage()} disabled={!canNextPage}>Next</button>
                <button onClick={() => gotoPage(pageCount - 1)} disabled={!canNextPage}>{'>>'}</button>
            </div>
        </>
    )
}