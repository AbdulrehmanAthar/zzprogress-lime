import http from 'k6/http';
import { check, sleep } from 'k6';

export default function () {
 
  let res = http.get('https://www.odoo.com/');
  check(res, {
    'Status is 200': (r) => r.status === 200,
  });

  
  res = http.get('https://www.odoo.com/page/website-builder');
  check(res, {
    'Status is 200': (r) => r.status === 200,
  });
  sleep(3); // Wait for 3 seconds before the next request

  res = http.get('https://www.odoo.com/page/accounting');
  check(res, {
    'Status is 200': (r) => r.status === 200,
  });
  sleep(3);

  res = http.get('https://www.odoo.com/page/hr');
  check(res, {
    'Status is 200': (r) => r.status === 200,
  });
  sleep(3);

 
  res = http.get('https://www.odoo.com/search?search=inventory');
  check(res, {
    'Status is 200': (r) => r.status === 200,
  });
  sleep(3);

  
  const payload = {
    name: 'John Doe',
    email: 'johndoe@example.com',
    message: 'This is a test message.',
  };
  res = http.post('https://www.odoo.com/contactus', payload);
  check(res, {
    'Status is 200': (r) => r.status === 200,
  });
  sleep(3);
}
