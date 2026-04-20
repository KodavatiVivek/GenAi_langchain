import { Injectable, inject } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

export interface IngestResponse {
  indexed_files: number;
  indexed_chunks: number;
  message: string;
}

export interface SourceDocument {
  source: string;
  page?: number | null;
  preview: string;
}

export interface AskResponse {
  answer: string;
  sources: SourceDocument[];
}

@Injectable({
  providedIn: 'root'
})
export class RagApiService {
  private readonly http = inject(HttpClient);
  private readonly baseUrl = 'http://localhost:8000/api';

  ingest(clearExisting = true): Observable<IngestResponse> {
    return this.http.post<IngestResponse>(`${this.baseUrl}/ingest`, {
      clear_existing: clearExisting
    });
  }

  ask(question: string): Observable<AskResponse> {
    return this.http.post<AskResponse>(`${this.baseUrl}/ask`, { question });
  }
}
