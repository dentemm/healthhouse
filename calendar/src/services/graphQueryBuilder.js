class GraphQueryBuilder {

  static showCount = (queryString) => {

    const query = '';

    if (!queryString || queryString !== '') {
      query += '?';
    }
    query += '$count=true';

    return query;
  }

  static addLimit = (queryString, limit) => {

    const query = '';

    if (!queryString || queryString !== '') {
      query += '?';
    }
    query += `$top=${limit}`;

    return query;
  }

  static addContent = (queryString, fieldList) => {

    const query = '';

    if (!queryString || queryString !== '') {
      query += '?';
    }

    query += `$select=${fieldList.join(',')}`;

    return query;
  }

  static orderBy = (queryString, field) => {

    const query = '';

    if (!queryString || queryString !== '') {
      query += '?';
    }

    query += `$orderBy=${field}`;

    return query;
  }

  static filterBy = (queryString, fieldName, comparator, reference) => {

    const query = '';

    if (!queryString || queryString !== '') {
      query += '?';
    }

    query += (`$filter=${fieldName} ${comparator} '${reference}'`).trim();

    return query;
  }
}