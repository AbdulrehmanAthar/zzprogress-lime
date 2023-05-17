import http from 'k6/http';
import { check, sleep } from 'k6';

export default function () {
  // Log in to Odoo.com
  const loginPayload = {
    jsonrpc: '2.0',
    method: 'call',
    id: 1,
    params: {
      service: 'common',
      method: 'login',
      args: ['your_username', 'your_password'],
    },
  };

  const loginHeaders = { 'Content-Type': 'application/json' };
  const loginRes = http.post('https://www.odoo.com/web/session/authenticate', JSON.stringify(loginPayload), { headers: loginHeaders });
  check(loginRes, {
    'Status is 200': (r) => r.status === 200,
  });

  // Extract the session ID from the login response
  const sessionId = loginRes.json().result.session_id;

  // Create a new record
  const createPayload = {
    jsonrpc: '2.0',
    method: 'call',
    id: 2,
    params: {
      service: 'object',
      method: 'execute',
      args: ['your_database', sessionId, 'your_password', 'your_model_name', 'create', { 'field_name': 'value' }],
      kwargs: {},
    },
  };

  const createRes = http.post('https://www.odoo.com/web/dataset/call_kw', JSON.stringify(createPayload), { headers: loginHeaders });
  check(createRes, {
    'Status is 200': (r) => r.status === 200,
    'Record created successfully': (r) => r.json().result > 0,
  });

  sleep(3);
}
